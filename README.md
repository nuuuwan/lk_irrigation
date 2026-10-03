# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_23:13:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,160 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 23:13:57 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.073 |  |
| 2026-10-03 23:09:04 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-03 23:08:56 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.182 |  |
| 2026-10-03 23:08:02 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-03 23:07:31 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-10-03 23:06:51 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:05:54 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-10-03 23:05:53 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:05:29 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:04:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:04:31 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:04:28 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-10-03 23:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-10-03 23:03:30 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:03:28 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:03:08 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-10-03 23:03:04 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-03 23:03:01 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-03 23:02:49 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:02:43 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-03 23:02:36 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.021 |  |
| 2026-10-03 23:02:23 | Peradeniya (Mahaweli Ganga) | 3.91 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-03 23:02:12 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.063 |  |
| 2026-10-03 23:02:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:04 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.036 |  |
| 2026-10-03 23:02:00 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-03 23:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:01:27 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:01:24 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:00:37 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:00:08 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-03 22:29:28 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.182 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 23:04:28 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-10-03 23:02:23 | Peradeniya (Mahaweli Ganga) | 3.91 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-03 23:03:04 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-03 23:02:00 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-03 23:08:02 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-03 23:00:37 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:01:27 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:06:51 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 22:03:12 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:43 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:03:30 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-03 22:09:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:05:29 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:04:31 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:03:28 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:01:24 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:02:36 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-03 22:23:02 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.007 |  |
| 2026-10-03 23:09:04 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-10-03 23:05:53 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:04:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:02:49 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-03 23:02:37 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-10-03 23:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.021 |  |
| 2026-10-03 23:05:54 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-10-03 23:07:31 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-10-03 23:03:57 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-10-03 23:02:04 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.036 |  |
| 2026-10-03 23:03:08 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-10-03 23:03:01 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-03 23:02:12 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.063 |  |
| 2026-10-03 23:13:57 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.073 |  |
| 2026-10-03 23:08:56 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)