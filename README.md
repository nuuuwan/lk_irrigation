# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_09:03:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 09:03:53 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:03:38 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:03:24 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:03:15 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:03:01 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.030 |  |
| 2026-11-14 09:02:42 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.041 |  |
| 2026-11-14 09:02:30 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-11-14 09:02:15 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:02:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:02:01 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:01:52 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:01:45 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:40 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:11 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:01:09 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:00:36 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:00:28 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:00:12 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 08:13:16 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 08:09:20 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.020 |  |
| 2026-11-14 09:02:42 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.041 |  |
| 2026-11-14 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | -0.082 |  |
| 2026-11-14 08:05:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-14 09:01:52 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:01:09 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:11:29 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:17 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:03:15 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:32 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:59 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:49 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:06:50 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:02:01 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:20:09 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 09:03:53 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-11-14 08:04:47 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-11-14 09:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:00:36 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:01:11 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:02:05 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:03:38 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:00:28 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-14 09:01:14 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:45 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-11-14 09:01:40 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-14 08:14:55 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:02:15 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-14 09:03:24 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:26 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:07:06 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:10:00 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.028 |  |
| 2026-11-14 09:03:01 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.030 |  |
| 2026-11-14 09:00:12 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.034 |  |
| 2026-11-14 09:02:30 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-11-14 08:05:38 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.075 |  |
| 2026-11-14 08:02:14 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)