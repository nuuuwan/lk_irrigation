# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_04:13:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,061 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 04:13:03 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:10:52 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:08:38 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.043 |  |
| 2026-04-18 04:08:27 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-04-18 04:06:52 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 04:06:51 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:06:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-04-18 04:06:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:06:36 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:06:04 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.003 |  |
| 2026-04-18 04:06:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-18 04:04:52 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:03:25 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:02:31 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.205 |  |
| 2026-04-18 04:02:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:02:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:02:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 04:01:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-18 04:01:54 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:00:57 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:00:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:00:50 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.043 |  |
| 2026-04-18 04:00:25 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-18 03:34:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:33:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:32:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:32:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:32:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:25:19 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.101 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 03:34:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 3.706 | 🔺 Rising |
| 2026-04-18 03:25:19 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-18 04:00:25 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-18 04:01:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-18 03:04:08 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 04:06:02 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-18 04:02:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 04:06:52 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 04:06:04 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.003 |  |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:00:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:02:26 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:13:03 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:03:25 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:08 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:01:54 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:06:36 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:06:51 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:04:52 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:10:52 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:06:30 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-18 04:08:27 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-04-18 04:02:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:02:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:00:57 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-04-18 04:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-18 00:03:00 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-04-18 00:03:24 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-04-18 04:08:38 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.043 |  |
| 2026-04-18 04:00:50 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.043 |  |
| 2026-04-18 04:06:51 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-04-18 04:02:31 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)