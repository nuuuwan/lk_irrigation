# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_07:14:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 07:14:24 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-10-22 07:13:04 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-22 07:11:41 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:10:11 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-10-22 07:08:52 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 07:08:28 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-10-22 07:07:42 | Galgamuwa (Mee Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:07:10 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.218 |  |
| 2026-10-22 07:06:26 | Rathnapura (Kalu Ganga) | 5.29 | 🟡 Alert | -0.113 |  |
| 2026-10-22 07:06:24 | Glencourse (Kelani Ganga) | 13.13 | 🟢 Normal | -0.208 |  |
| 2026-10-22 07:06:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 07:06:22 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.232 |  |
| 2026-10-22 07:06:14 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-22 07:06:06 | Moragaswewa (Deduru Oya) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:05:30 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 07:05:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-10-22 07:05:00 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-22 07:04:57 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.002 |  |
| 2026-10-22 07:04:57 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 07:04:45 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-10-22 07:04:36 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-22 07:04:32 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-22 07:04:29 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.057 |  |
| 2026-10-22 07:04:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:03:45 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.142 |  |
| 2026-10-22 07:03:38 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-22 07:03:12 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.062 |  |
| 2026-10-22 07:03:04 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-10-22 07:03:04 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-10-22 07:03:01 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 07:02:59 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-10-22 07:02:10 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.102 |  |
| 2026-10-22 07:02:05 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-10-22 07:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-10-22 07:01:02 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.143 |  |
| 2026-10-22 07:00:15 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-22 07:00:11 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.110 |  |
| 2026-10-22 06:45:42 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.232 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 07:06:26 | Rathnapura (Kalu Ganga) | 5.29 | 🟡 Alert | -0.113 |  |
| 2026-10-22 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-10-22 07:05:00 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-22 07:06:14 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-22 07:13:04 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-22 07:04:36 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-22 07:06:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 07:08:52 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 07:03:01 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 07:02:59 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 07:04:57 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 07:05:30 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 07:04:57 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.002 |  |
| 2026-10-22 07:06:06 | Moragaswewa (Deduru Oya) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:07:42 | Galgamuwa (Mee Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-10-22 06:01:37 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:04:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:11:41 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-22 07:14:24 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-10-22 07:05:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2026-10-22 07:10:11 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-10-22 07:04:32 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-22 07:03:38 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-10-22 07:04:45 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-10-22 07:02:05 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-10-22 07:03:04 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-10-22 07:03:04 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.039 |  |
| 2026-10-22 07:00:15 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-10-22 07:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-10-22 07:08:28 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-10-22 07:04:29 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.057 |  |
| 2026-10-22 07:03:12 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.062 |  |
| 2026-10-22 07:02:10 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.102 |  |
| 2026-10-22 07:00:11 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.110 |  |
| 2026-10-22 07:03:45 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.142 |  |
| 2026-10-22 07:01:02 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.143 |  |
| 2026-10-22 07:06:24 | Glencourse (Kelani Ganga) | 13.13 | 🟢 Normal | -0.208 |  |
| 2026-10-22 07:07:10 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.218 |  |
| 2026-10-22 07:06:22 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)