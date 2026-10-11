# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_20:08:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 20:08:23 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-11 20:07:23 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.037 |  |
| 2026-10-11 20:06:21 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-11 20:06:17 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 20:06:08 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-11 20:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.021 |  |
| 2026-10-11 20:05:23 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-11 20:04:47 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-10-11 20:04:25 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.091 |  |
| 2026-10-11 20:04:17 | Hanwella (Kelani Ganga) | 2.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-11 20:04:14 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-10-11 20:03:58 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-11 20:03:55 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.277 |  |
| 2026-10-11 20:03:33 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 20:03:21 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 20:03:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 20:02:18 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-11 20:02:14 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 20:02:03 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 20:01:55 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 20:01:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-11 20:01:31 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-10-11 20:01:24 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-11 20:01:17 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-11 20:01:09 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 20:00:27 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:00:18 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 20:01:31 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-10-11 20:04:14 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-10-11 20:04:47 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-10-11 20:05:23 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-11 19:01:56 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-11 20:06:08 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-10-11 20:01:24 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-11 19:11:53 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-11 20:03:33 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 20:04:17 | Hanwella (Kelani Ganga) | 2.71 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-11 19:15:33 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 20:03:21 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 20:03:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 20:01:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-11 20:08:23 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-11 19:05:20 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-11 20:01:09 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 20:02:14 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 20:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 20:01:55 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 20:02:03 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:04:25 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:00:27 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 20:00:18 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-11 20:01:17 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-11 20:03:58 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-11 20:02:18 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-10-11 19:06:29 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-11 20:06:21 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-11 20:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.021 |  |
| 2026-10-11 20:06:17 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-10-11 20:07:23 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.037 |  |
| 2026-10-11 19:06:44 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.079 |  |
| 2026-10-11 19:03:22 | Moragaswewa (Deduru Oya) | 2.07 | 🟢 Normal | -0.087 |  |
| 2026-10-11 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.091 |  |
| 2026-10-11 20:03:55 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.277 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)