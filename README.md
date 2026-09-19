# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_10:15:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,044 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 10:15:14 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-19 10:08:28 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-09-19 10:07:41 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-19 10:07:17 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:06:46 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.029 |  |
| 2026-09-19 10:06:45 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-19 10:06:40 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:06:02 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-09-19 10:05:48 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:05:13 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:05:08 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-09-19 10:04:55 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.041 |  |
| 2026-09-19 10:04:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 10:04:28 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:01 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-09-19 10:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:03:24 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-19 10:03:08 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-09-19 10:03:01 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:41 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:40 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-09-19 10:02:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 10:02:36 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:26 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-09-19 10:02:22 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:20 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.080 |  |
| 2026-09-19 10:02:19 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:02:12 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:01:50 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 10:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:00:56 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-09-19 10:00:44 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:00:39 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 10:04:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 10:07:41 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-19 10:15:14 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-19 10:01:50 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 10:02:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 10:06:40 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:22 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:00:44 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 09:02:28 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:24 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:00:39 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:41 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:03:01 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:01 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:05:48 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:05:13 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:04:28 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:07:17 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:36 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 10:02:19 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:02:12 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.010 |  |
| 2026-09-19 10:03:08 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.012 |  |
| 2026-09-19 10:08:28 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.019 |  |
| 2026-09-19 10:02:40 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-09-19 10:02:26 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-09-19 10:00:56 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-09-19 10:06:46 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.029 |  |
| 2026-09-19 10:03:24 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-19 10:06:45 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-19 10:05:08 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-09-19 10:06:02 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-09-19 10:04:55 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.041 |  |
| 2026-09-19 10:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-09-19 10:02:20 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)