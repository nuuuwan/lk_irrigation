# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_06:19:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,344 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 06:19:45 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:14:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-11-14 06:12:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-11-14 06:10:05 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.063 |  |
| 2026-11-14 06:08:39 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-11-14 06:08:31 | Baddegama (Gin Ganga) | 3.73 | 🟡 Alert | -0.036 |  |
| 2026-11-14 06:06:58 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:06:56 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.076 |  |
| 2026-11-14 06:06:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:06:04 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:06:01 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-14 06:05:52 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 06:04:47 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-14 06:04:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:04:27 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-14 06:03:32 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:03:12 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:02:54 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.050 |  |
| 2026-11-14 06:02:43 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-11-14 06:02:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.072 |  |
| 2026-11-14 06:02:33 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.066 |  |
| 2026-11-14 06:02:31 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.020 |  |
| 2026-11-14 06:02:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-11-14 06:01:54 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:42 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:40 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -4.828 |  |
| 2026-11-14 06:01:38 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:01:33 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:33 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 06:01:24 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-14 06:01:14 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.023 |  |
| 2026-11-14 06:01:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.064 |  |
| 2026-11-14 06:00:47 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:00:32 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-14 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 06:01:24 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-14 06:08:31 | Baddegama (Gin Ganga) | 3.73 | 🟡 Alert | -0.036 |  |
| 2026-11-14 06:00:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.064 |  |
| 2026-11-14 06:06:56 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.076 |  |
| 2026-11-14 06:04:47 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-14 06:01:33 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 06:05:52 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 06:01:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:42 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:54 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:06:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:04:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:00:47 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:03:32 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:33 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:19:45 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:04:27 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-14 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:01:38 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:03:12 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:12:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-11-14 06:08:39 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-11-14 06:06:01 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-14 06:02:43 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-11-14 06:02:31 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.020 |  |
| 2026-11-14 06:00:32 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-14 06:01:14 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.023 |  |
| 2026-11-14 05:11:29 | Moraketiya (Walawe Ganga) | 2.85 | 🟢 Normal | -0.023 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:06:04 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:06:58 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:14:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-11-14 06:02:54 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.050 |  |
| 2026-11-14 06:10:05 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.063 |  |
| 2026-11-14 06:02:33 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.066 |  |
| 2026-11-14 06:02:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-11-14 06:02:41 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.072 |  |
| 2026-11-14 06:01:40 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -4.828 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)