# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_10:03:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 10:03:56 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-10-30 10:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-30 10:03:35 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.042 |  |
| 2026-10-30 10:03:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 10:03:26 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.030 |  |
| 2026-10-30 10:02:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:02:16 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 10:02:15 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-30 10:01:59 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-10-30 10:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:01:48 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.057 |  |
| 2026-10-30 10:00:54 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:41 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-30 10:00:35 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-30 10:00:12 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-30 10:00:09 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 09:00:55 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 09:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-30 09:09:28 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | -0.029 |  |
| 2026-10-30 09:02:46 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-10-30 10:01:48 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.057 |  |
| 2026-10-30 09:02:24 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-30 10:00:12 | Weraganthota (Mahaweli Ganga) | -2.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-30 09:02:51 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 10:02:16 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 10:03:35 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 10:00:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-30 10:00:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:54 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:12:16 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:00:09 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:00:41 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 10:02:57 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:02:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:05:12 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-30 09:10:22 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.009 |  |
| 2026-10-30 10:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-30 10:00:41 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:02:14 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:01:13 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-30 09:04:13 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-30 10:01:59 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-10-30 10:02:15 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2026-10-30 09:04:56 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.029 |  |
| 2026-10-30 10:03:26 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.030 |  |
| 2026-10-30 10:03:56 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-10-30 10:03:35 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.042 |  |
| 2026-10-30 09:09:19 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.045 |  |
| 2026-10-30 09:11:07 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.052 |  |
| 2026-10-30 09:04:13 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.052 |  |
| 2026-10-30 09:08:30 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | -0.064 |  |
| 2026-10-30 09:01:35 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.081 |  |
| 2026-10-30 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-10-30 09:04:28 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.791 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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