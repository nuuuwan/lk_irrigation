# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_21:22:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,059 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 21:22:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-15 21:09:35 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.046 |  |
| 2026-04-15 21:07:07 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:06:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:06:07 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:05:50 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:05:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:05:18 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.029 |  |
| 2026-04-15 21:05:08 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:04:46 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-04-15 21:04:28 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-15 21:04:17 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:04:13 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.656 | 🔺 Rising |
| 2026-04-15 21:04:06 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:03:51 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:03:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:03:22 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-15 21:03:13 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:02:55 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-15 21:02:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-15 21:02:30 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:02:24 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:07 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:04 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:01:57 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:01:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:01:18 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-15 21:01:06 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:01:03 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-15 21:00:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:00:38 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-15 21:00:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.243 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 21:04:13 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.656 | 🔺 Rising |
| 2026-04-15 21:00:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-04-15 21:04:28 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-15 21:02:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-15 21:03:22 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-15 21:22:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-15 21:00:38 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-15 21:05:50 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:06:19 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:00:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:55 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:04:17 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:30 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:03:51 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:05:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:07 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:03:24 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:01:06 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:24 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:07:07 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:01:57 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:05:08 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:23:36 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:04:06 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-15 21:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:03:13 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:06:07 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:01:30 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 21:01:18 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-15 19:00:35 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-04-15 21:01:03 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-04-15 21:04:46 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-04-15 21:05:18 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.029 |  |
| 2026-04-15 21:02:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 21:09:35 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.046 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)