# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_09:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,095 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 09:13:05 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:11:46 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:11:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:07:32 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:07:05 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:06:46 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-12 09:06:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:06:35 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:06:29 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 09:06:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:06:19 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:05:54 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-07-12 09:05:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:04:48 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:04:41 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:04:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-12 09:04:21 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -47.284 |  |
| 2026-07-12 09:04:05 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-12 09:03:58 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:03:49 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-12 09:03:33 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-12 09:03:14 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -47.284 |  |
| 2026-07-12 09:03:12 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:02:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.435 |  |
| 2026-07-12 09:02:52 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-07-12 09:02:42 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.055 |  |
| 2026-07-12 09:02:39 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.020 |  |
| 2026-07-12 09:02:38 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:02:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-07-12 09:02:04 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-12 09:01:43 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:31 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-07-12 09:01:15 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:01:08 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:03 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:00:23 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:00:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:46:06 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 09:06:46 | Nagalagam Street (Kelani Ganga) | 0.32 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-12 09:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-07-12 09:02:04 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-12 09:03:49 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-12 09:04:05 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-12 09:06:29 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-12 09:04:33 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-12 09:01:43 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:08 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:00:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:13:05 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:11:46 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:07:32 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:02:38 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:06:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:07:05 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:01:03 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:03:12 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:11:18 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:00:23 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:05:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:04:41 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:07:52 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 09:03:33 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-12 09:06:19 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:04:48 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:06:35 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:03:58 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-07-12 09:02:14 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-07-12 09:02:39 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.020 |  |
| 2026-07-12 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:01:15 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:05:54 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.021 |  |
| 2026-07-12 09:01:31 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-07-12 09:02:52 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-07-12 09:02:42 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.055 |  |
| 2026-07-12 09:02:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.435 |  |
| 2026-07-12 09:04:21 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -47.284 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)