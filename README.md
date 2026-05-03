# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_16:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,891 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 16:03:22 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 16:03:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.032 |  |
| 2026-05-03 16:02:50 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-03 16:02:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:34 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 16:02:23 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:07 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:46 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:30 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.053 |  |
| 2026-05-03 16:01:29 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:01:23 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:01:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:06 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.051 |  |
| 2026-05-03 16:00:42 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.078 |  |
| 2026-05-03 16:00:16 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.020 |  |
| 2026-05-03 15:14:15 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 15:03:13 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-03 16:02:34 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-03 15:07:28 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-03 16:03:22 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 16:01:33 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:46 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:00:06 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:24 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:04:48 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:29 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:01:49 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:02:27 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:03:17 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:02:23 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:07:49 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:07:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 16:01:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 15:10:27 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-05-03 15:00:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:01:29 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:01:23 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:02:07 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:00:16 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.020 |  |
| 2026-05-03 16:02:50 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-03 16:03:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.032 |  |
| 2026-05-03 15:04:41 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.032 |  |
| 2026-05-03 15:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-05-03 15:02:56 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.045 |  |
| 2026-05-03 16:01:06 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.051 |  |
| 2026-05-03 16:01:30 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.053 |  |
| 2026-05-03 15:02:24 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.055 |  |
| 2026-05-03 16:00:42 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)