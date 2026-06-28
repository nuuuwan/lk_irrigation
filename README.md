# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_18:20:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 18:20:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-28 18:14:41 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-28 18:07:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.044 |  |
| 2026-06-28 18:07:05 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.028 |  |
| 2026-06-28 18:06:48 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:06:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:05:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.106 |  |
| 2026-06-28 18:05:28 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:57 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 18:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 18:03:54 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 18:03:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:36 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:13 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:12 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:12 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:36 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:29 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:02:24 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:02:23 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-28 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 18:02:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:07 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:06 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:57 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:35 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 18:01:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:18 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-28 18:01:05 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:02 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:00:15 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 18:05:28 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-28 18:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 18:20:29 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-28 18:02:23 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-28 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 18:03:54 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 18:04:14 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 18:01:35 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 18:14:41 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-28 18:06:48 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:05 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:57 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:12 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:12 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:02 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:07 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:13 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:03:36 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:06:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:36 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:57 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:06 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:02:24 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:02:29 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:18 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-06-28 18:01:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-28 18:07:05 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.028 |  |
| 2026-06-28 18:00:15 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2026-06-28 18:07:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.044 |  |
| 2026-06-28 18:05:59 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)