# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_19:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,301 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 19:18:08 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-12 19:15:12 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.011 |  |
| 2026-04-12 19:12:07 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-12 19:09:39 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:09:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:08:09 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 19:06:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-04-12 19:06:18 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-12 19:06:02 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:05:44 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:05:38 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 19:05:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:05:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.102 |  |
| 2026-04-12 19:04:54 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:04:33 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:04:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:04:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:04:04 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:03:46 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-12 19:03:16 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-12 19:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-12 19:03:09 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 19:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-04-12 19:02:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:02:24 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:02:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:01:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-12 19:01:50 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:01:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 19:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 19:01:11 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:01:11 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 19:00:40 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:00:14 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:00:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 18:34:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 19:03:46 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-12 19:18:08 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-12 19:01:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-12 19:03:16 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-12 19:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-12 19:12:07 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-12 19:03:09 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 19:01:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 19:05:38 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 19:01:11 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 19:06:18 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-12 19:01:43 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 19:04:54 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:00:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:04:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:05:44 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:05:31 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 19:08:09 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 19:00:14 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:09:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:06:02 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:10:30 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:01:11 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:04:04 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:04:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:02:24 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:00:40 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:02:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:09:39 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:02:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:01:50 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:04:33 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-12 19:15:12 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.011 |  |
| 2026-04-12 19:06:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-04-12 19:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 19:05:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)