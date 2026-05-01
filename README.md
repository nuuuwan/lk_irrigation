# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_19:23:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 19:23:25 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-01 19:16:55 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.017 |  |
| 2026-05-01 19:15:15 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:09:34 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 19:08:12 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-01 19:07:43 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.091 |  |
| 2026-05-01 19:07:16 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 19:07:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.023 |  |
| 2026-05-01 19:07:02 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:06:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-05-01 19:06:21 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-05-01 19:04:56 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-05-01 19:04:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:04:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:04:16 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 19:03:56 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.012 |  |
| 2026-05-01 19:03:47 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.076 |  |
| 2026-05-01 19:03:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 19:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:53 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:02:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:10 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:04 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-01 19:01:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-05-01 19:01:53 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:51 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:44 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-05-01 19:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:29 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 19:02:04 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-01 19:23:25 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-01 19:03:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-01 19:08:12 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-01 19:07:16 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 19:00:46 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-01 19:04:16 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 19:09:34 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 19:00:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:15:15 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:04:22 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:47 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:51 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:00:12 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:02:53 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:07:02 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:01:29 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 19:04:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:53 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:26 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:02:10 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:00:38 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:03:56 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.012 |  |
| 2026-05-01 19:16:55 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.017 |  |
| 2026-05-01 19:04:56 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-05-01 19:06:45 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-05-01 19:01:44 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-05-01 19:07:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.023 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 19:06:21 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-05-01 19:01:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-05-01 19:03:47 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.076 |  |
| 2026-05-01 19:07:43 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)