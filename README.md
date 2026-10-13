# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_03:04:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,267 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 03:04:11 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.076 |  |
| 2026-10-14 03:04:02 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.171 |  |
| 2026-10-14 03:03:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-14 03:03:42 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-14 03:03:23 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -1.500 |  |
| 2026-10-14 03:03:19 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.189 |  |
| 2026-10-14 03:03:16 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:03:02 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-14 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | -0.021 |  |
| 2026-10-14 03:02:43 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 03:02:40 | Ellagawa (Kalu Ganga) | 7.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 03:02:38 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:35 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -1.500 |  |
| 2026-10-14 03:02:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-14 03:02:13 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:07 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.101 |  |
| 2026-10-14 03:01:56 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:01:10 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:01:08 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-10-14 03:00:47 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:50:14 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-10-14 02:46:05 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.023 |  |
| 2026-10-14 02:41:09 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.189 |  |
| 2026-10-14 02:37:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-14 02:32:22 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-14 02:25:21 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:22:09 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 02:06:34 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2026-10-14 02:04:09 | Magura (Kalu Ganga) | 5.19 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-10-14 03:01:08 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-10-14 02:37:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-14 03:03:42 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-14 03:03:02 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-14 02:22:09 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-14 03:02:43 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 03:02:40 | Ellagawa (Kalu Ganga) | 7.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 02:05:06 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-14 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-14 02:04:51 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 02:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 02:06:40 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 02:06:38 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:31 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:00:47 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:08:17 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:03:16 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:04:02 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:03:06 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:01:56 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:38 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-14 03:02:13 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 02:02:01 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 03:03:55 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:06:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | -0.021 |  |
| 2026-10-14 02:46:05 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.023 |  |
| 2026-10-14 02:50:14 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-10-14 01:00:31 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.066 |  |
| 2026-10-14 03:04:11 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.076 |  |
| 2026-10-14 03:02:07 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.101 |  |
| 2026-10-14 03:04:02 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.171 |  |
| 2026-10-14 03:03:19 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.189 |  |
| 2026-10-14 03:03:23 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)