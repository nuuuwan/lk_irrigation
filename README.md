# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_01:18:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 01:18:34 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-04 01:15:15 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-06-04 01:12:49 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 01:07:25 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:07:23 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:07:22 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:06:43 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-04 01:06:33 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:06:29 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 01:06:24 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-04 01:06:10 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:05:28 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 01:05:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:04:42 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-06-04 01:04:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:57 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 01:03:47 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:12 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:02 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:02:23 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-04 01:02:18 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 01:02:16 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-04 01:02:13 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 01:02:12 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:02:11 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 01:02:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:47 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 01:01:18 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-04 01:01:17 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 00:04:42 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 00:59:52 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-06-04 01:02:13 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 01:01:18 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-04 01:06:24 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-04 01:06:43 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-04 01:12:49 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 01:06:29 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 01:18:34 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-04 01:02:16 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-04 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 01:00:46 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 01:05:28 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 01:02:23 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-04 01:02:18 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 01:02:11 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 01:03:57 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:07:25 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:06:10 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:02:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:00:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:06:33 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:47 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:02:12 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:12 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:05:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:01:17 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:03 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:44 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:03:47 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:04:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:06:47 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-04 01:04:42 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-06-04 01:15:15 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.019 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)