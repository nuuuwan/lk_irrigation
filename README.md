# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_19:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 19:17:18 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.026 |  |
| 2026-02-19 19:12:34 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:12:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:11:05 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 19:10:43 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:09:07 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 19:07:54 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.055 |  |
| 2026-02-19 19:07:50 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:51 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:05:58 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:05:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 19:05:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.095 |  |
| 2026-02-19 19:05:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 19:04:41 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-19 19:04:36 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:04:28 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:04:14 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.100 |  |
| 2026-02-19 19:03:58 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-19 19:03:52 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:03:45 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-02-19 19:03:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -8.151 |  |
| 2026-02-19 19:03:11 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 19:03:10 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-19 19:03:00 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-02-19 19:02:47 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:02:29 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:02:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-19 19:02:12 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:01:45 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 19:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:00:28 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-19 19:00:27 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:00:25 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -8.151 |  |
| 2026-02-19 19:00:24 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 19:03:00 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-02-19 18:04:32 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-19 19:03:58 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-19 19:04:41 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-19 19:03:11 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 19:03:10 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-19 19:00:24 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-19 19:00:28 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-19 19:05:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 19:09:07 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 19:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 19:01:45 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 19:11:05 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 19:02:47 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:00:27 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:10:43 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:04:28 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:03:52 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:03:40 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:02:12 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:07:50 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:51 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:04:36 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:12:34 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:12:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:05:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:05:58 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 18:01:54 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:06:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:02:29 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 19:02:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-19 19:03:45 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-02-19 19:17:18 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.026 |  |
| 2026-02-19 19:07:54 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.055 |  |
| 2026-02-19 19:05:09 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.095 |  |
| 2026-02-19 19:04:14 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.100 |  |
| 2026-02-19 19:03:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -8.151 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)