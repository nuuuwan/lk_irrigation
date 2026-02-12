# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_19:24:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 19:24:47 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-12 19:19:52 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:18:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:15:17 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:12:58 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:09:58 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:09:34 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-12 19:08:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:07:50 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-12 19:06:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:06:19 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:06:02 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-12 19:05:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-02-12 19:05:31 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:04:58 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 19:04:33 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-12 19:04:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-12 19:04:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:04:07 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-02-12 19:03:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:03:16 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:02:56 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:02:47 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:02:47 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-12 19:02:45 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:02:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:01:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:01:33 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:01:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 19:01:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:00:59 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:00:11 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 19:04:07 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-02-12 19:05:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-02-12 19:24:47 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-12 19:07:50 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-12 19:09:34 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-12 19:04:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-12 19:01:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 19:04:58 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 19:02:45 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:01:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:03:16 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 19:02:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:04:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:02:47 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:00:59 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:03:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:09:58 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:00:11 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:08:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:18:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:15:17 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:16:22 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:12:58 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:01:33 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:01:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:02:56 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:06:19 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:05:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:19:52 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:06:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 19:04:33 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-12 19:02:47 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-12 19:06:02 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-12 18:02:22 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-12 18:11:57 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.017 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)