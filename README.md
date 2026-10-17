# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_23:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 23:03:04 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-17 23:03:00 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-17 23:02:38 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.024 |  |
| 2026-10-17 23:02:36 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | 1.022 | 🔺 Rising |
| 2026-10-17 23:02:34 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-17 23:02:23 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.061 |  |
| 2026-10-17 23:02:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:02:10 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.847 |  |
| 2026-10-17 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.226 |  |
| 2026-10-17 23:01:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 23:01:24 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.158 |  |
| 2026-10-17 23:00:51 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:00:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-17 22:19:27 | Urawa (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-17 22:17:19 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 23:03:04 | Panadugama (Nilwala Ganga) | 6.18 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-17 22:17:19 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 22:02:19 | Rathnapura (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-10-17 22:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.48 | 🟡 Alert | -0.019 |  |
| 2026-10-17 23:02:23 | Norwood (Kelani Ganga) | 1.60 | 🟡 Alert | -0.061 |  |
| 2026-10-17 23:02:36 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | 1.022 | 🔺 Rising |
| 2026-10-17 22:01:35 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-10-17 22:07:35 | Thaldena (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-17 23:00:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-17 23:03:00 | Glencourse (Kelani Ganga) | 13.30 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-17 22:04:11 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-17 22:04:23 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-17 22:04:22 | Pitabeddara (Nilwala Ganga) | 3.48 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-17 22:19:27 | Urawa (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-17 22:01:54 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-17 22:03:57 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 23:01:34 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:02:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:50 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:00:51 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 22:02:09 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-17 23:01:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-17 23:02:34 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-17 22:02:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-10-17 22:03:26 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-17 23:02:38 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.024 |  |
| 2026-10-17 22:04:39 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-10-17 22:01:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.034 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 22:10:10 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.043 |  |
| 2026-10-17 22:06:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-10-17 23:01:24 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.158 |  |
| 2026-10-17 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.226 |  |
| 2026-10-17 22:05:31 | Holombuwa (Kelani Ganga) | 2.70 | 🟢 Normal | -0.451 |  |
| 2026-10-17 23:02:10 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.847 |  |
| 2026-10-17 22:06:07 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -1.407 |  |
| 2026-10-17 21:06:08 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)