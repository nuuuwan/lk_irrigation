# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_08:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 08:02:56 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-11-14 08:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:26 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | -0.082 |  |
| 2026-11-14 08:02:14 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:14 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |
| 2026-11-14 08:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.044 |  |
| 2026-11-14 08:01:23 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:00:27 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:00:19 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:37:44 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 06:01:24 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-14 07:09:59 | Baddegama (Gin Ganga) | 3.70 | 🟡 Alert | -0.029 |  |
| 2026-11-14 07:04:48 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | -0.062 |  |
| 2026-11-14 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | -0.082 |  |
| 2026-11-14 07:00:30 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-14 07:06:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-14 07:05:16 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 07:05:45 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-14 07:01:25 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:00:19 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:20 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:05:06 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:04:20 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:37:44 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:02:12 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-11-14 07:09:26 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.009 |  |
| 2026-11-14 07:07:20 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-11-14 07:07:11 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-11-14 07:02:31 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:01:14 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-14 08:02:14 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:00:27 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:26 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-14 07:06:16 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.028 |  |
| 2026-11-14 08:01:23 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.044 |  |
| 2026-11-14 07:08:32 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.044 |  |
| 2026-11-14 07:13:24 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.047 |  |
| 2026-11-14 07:04:12 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.072 |  |
| 2026-11-14 07:05:21 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.082 |  |
| 2026-11-14 07:01:46 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.102 |  |
| 2026-11-14 08:02:14 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |
| 2026-11-14 07:05:51 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.132 |  |
| 2026-11-14 07:07:23 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.139 |  |
| 2026-11-14 07:01:39 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.517 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)