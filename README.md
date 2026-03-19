# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_03:11:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 03:11:37 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.139 |  |
| 2026-03-20 03:10:38 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 03:09:02 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-20 03:08:31 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-03-20 03:07:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-20 03:06:48 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-20 03:06:04 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-20 03:05:52 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:05:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:05:05 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 03:04:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.058 |  |
| 2026-03-20 03:04:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:03:52 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:03:44 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.045 |  |
| 2026-03-20 03:03:14 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.026 |  |
| 2026-03-20 03:03:09 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 03:02:50 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:34 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:32 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:26 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.020 |  |
| 2026-03-20 03:02:26 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:08 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-20 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-20 03:01:40 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-20 03:01:40 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-03-20 03:01:37 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 03:06:48 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 03:07:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-20 03:09:02 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-20 03:01:40 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-20 03:06:04 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-20 02:03:27 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 03:05:05 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-20 03:03:09 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 03:10:38 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 03:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:34 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:50 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-20 02:03:15 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:04:11 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:26 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:05:22 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:03:52 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:32 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:05:52 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-20 03:02:08 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-20 03:08:31 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-03-20 03:01:40 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-03-20 03:02:26 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.020 |  |
| 2026-03-20 03:03:14 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.026 |  |
| 2026-03-20 03:03:44 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.045 |  |
| 2026-03-20 03:04:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.058 |  |
| 2026-03-20 03:01:37 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.080 |  |
| 2026-03-20 02:00:52 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.128 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-20 03:11:37 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.139 |  |
| 2026-03-20 02:20:13 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)