# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_10:31:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 10:31:09 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:16:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:15:47 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:12:14 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:12:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-06-04 10:10:32 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-06-04 10:09:32 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-04 10:08:18 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-04 10:07:35 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-04 10:07:01 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:06:07 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:06:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:06:01 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:05:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:05:26 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:05:11 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-04 10:05:02 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.039 |  |
| 2026-06-04 10:04:54 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-06-04 10:04:51 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:04:49 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-06-04 10:04:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:04:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:04:04 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 10:03:53 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:46 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:03:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:17 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-06-04 10:03:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-04 10:02:40 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 10:02:39 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.040 |  |
| 2026-06-04 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 10:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-04 10:08:18 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-04 10:05:11 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-04 10:07:35 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-04 10:01:37 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 10:04:04 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 10:09:32 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-04 10:02:01 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-04 10:02:40 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 10:04:51 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:06:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:03:46 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 10:01:02 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:05:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:06:01 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:04:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:37 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:15:47 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:12:14 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:04:11 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:01:43 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:01:48 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:02:10 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:06:07 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:31:09 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:01:09 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:16:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:03:53 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 10:10:32 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.009 |  |
| 2026-06-04 10:12:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-06-04 10:03:17 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-06-04 10:04:49 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-06-04 10:05:02 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.039 |  |
| 2026-06-04 10:02:39 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.040 |  |
| 2026-06-04 10:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.050 |  |
| 2026-06-04 10:04:54 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)