# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_09:04:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 09:04:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.791 |  |
| 2026-10-30 09:04:13 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.052 |  |
| 2026-10-30 09:04:13 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:03:39 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:57 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.040 |  |
| 2026-10-30 09:02:57 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.791 |  |
| 2026-10-30 09:02:54 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:51 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 09:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-10-30 09:02:46 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-10-30 09:02:28 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:24 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-30 09:02:16 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:14 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:01:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:01:35 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.081 |  |
| 2026-10-30 09:01:13 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:00:55 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 09:00:51 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:00:48 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-10-30 09:00:41 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 09:00:55 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 08:09:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-30 09:02:46 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-10-30 08:06:22 | Baddegama (Gin Ganga) | 3.53 | 🟡 Alert | -0.037 |  |
| 2026-10-30 08:06:13 | Panadugama (Nilwala Ganga) | 5.55 | 🟡 Alert | -0.048 |  |
| 2026-10-30 09:00:48 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-10-30 09:02:24 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-30 09:02:51 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 09:03:39 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:13 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:02:36 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:54 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:00:41 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:16 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:08:20 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:28 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-30 08:03:48 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:00:51 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:02:14 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:05:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:01:13 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:04:13 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:01:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-30 08:03:13 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-10-30 08:03:33 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-10-30 08:05:41 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-30 08:03:22 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.033 |  |
| 2026-10-30 08:02:33 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-10-30 09:02:57 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.040 |  |
| 2026-10-30 08:13:34 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.047 |  |
| 2026-10-30 08:12:03 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.050 |  |
| 2026-10-30 09:04:13 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.052 |  |
| 2026-10-30 08:02:34 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.063 |  |
| 2026-10-30 09:01:35 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.081 |  |
| 2026-10-30 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-10-30 09:04:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.791 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)