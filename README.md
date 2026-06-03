# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_04:01:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,867 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 04:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:39 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.091 |  |
| 2026-06-04 04:01:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:10 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:00:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:56:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 03:47:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 03:46:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 03:46:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 03:27:44 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 03:23:57 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:16:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-06-04 03:15:59 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 03:10:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:09:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 03:47:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 03:02:53 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | 1.403 | 🔺 Rising |
| 2026-06-04 03:03:50 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-06-04 03:05:08 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-04 03:56:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 03:02:35 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-04 03:08:02 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-04 03:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-04 03:15:59 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 03:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-04 03:06:06 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-04 03:04:31 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 03:04:58 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 03:03:39 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 03:01:14 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 03:04:40 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 03:04:34 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:00:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:10 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:31 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:28 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:01:43 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:08:04 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:10:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:05:06 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:09:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 04:01:39 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:23:57 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:05:30 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:16:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-06-04 03:04:38 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-06-04 04:01:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)