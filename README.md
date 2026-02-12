# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_06:17:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 06:17:57 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-12 06:14:08 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:13:22 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.005 |  |
| 2026-02-12 06:11:17 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:10:10 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:07:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:06:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:06:38 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 06:06:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.029 |  |
| 2026-02-12 06:06:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.033 |  |
| 2026-02-12 06:05:55 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:52 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-02-12 06:04:56 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:04:44 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 06:04:33 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 06:04:19 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-02-12 06:04:08 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 06:03:53 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:23 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:11 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-12 06:03:04 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 06:02:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:02:19 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 06:02:04 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.027 |  |
| 2026-02-12 06:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-02-12 06:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-02-12 06:01:09 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.014 |  |
| 2026-02-12 06:01:08 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:00:20 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.051 |  |
| 2026-02-12 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 05:56:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-02-12 05:46:13 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.029 |  |
| 2026-02-12 05:28:06 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 06:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-02-12 06:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-02-12 06:17:57 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-12 06:03:11 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-12 06:04:44 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 06:06:38 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 06:04:08 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 06:02:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 06:04:33 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 06:03:04 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 06:01:08 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:53 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:23 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:14:08 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:00:16 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:06:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:04:56 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:55 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:07:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:11:17 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:03:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:10:10 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:02:40 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:05:52 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 06:13:22 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.005 |  |
| 2026-02-12 06:04:19 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | -0.010 |  |
| 2026-02-12 06:02:19 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 06:01:09 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.014 |  |
| 2026-02-12 06:02:04 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.027 |  |
| 2026-02-12 06:06:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.029 |  |
| 2026-02-12 06:06:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.033 |  |
| 2026-02-12 06:00:20 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.051 |  |
| 2026-02-12 06:05:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)