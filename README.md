# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_13:17:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,485 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 13:17:57 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.026 |  |
| 2026-06-30 13:17:26 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.042 |  |
| 2026-06-30 13:14:06 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:13:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:11:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:09:30 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:08:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:07:49 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:06:31 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.136 |  |
| 2026-06-30 13:06:10 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:06:07 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-06-30 13:05:49 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:05:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:05:01 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 13:04:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.073 |  |
| 2026-06-30 13:04:56 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-06-30 13:04:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.041 |  |
| 2026-06-30 13:04:37 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.144 |  |
| 2026-06-30 13:03:41 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.080 |  |
| 2026-06-30 13:03:39 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-30 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-06-30 13:03:10 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:03:05 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:03:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-30 13:03:03 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:03:01 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:57 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:36 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 13:02:34 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:28 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:02:19 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.039 |  |
| 2026-06-30 13:02:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-06-30 13:01:59 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-06-30 13:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:01:18 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 13:01:05 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.072 |  |
| 2026-06-30 13:00:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 13:03:03 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-30 13:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-30 13:01:18 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 13:02:36 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 13:05:01 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 13:03:05 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:01:59 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:08:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:09:30 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:14:06 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:11:37 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:03:39 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:13:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:34 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:57 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:00:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:02:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:06:10 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 13:05:49 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:07:49 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:05:13 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:03:10 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:02:28 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:03:03 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-30 13:04:56 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-06-30 13:06:07 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-06-30 13:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-06-30 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.021 |  |
| 2026-06-30 13:17:57 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.026 |  |
| 2026-06-30 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-06-30 13:02:19 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.039 |  |
| 2026-06-30 13:04:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.041 |  |
| 2026-06-30 13:17:26 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.042 |  |
| 2026-06-30 13:01:05 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.072 |  |
| 2026-06-30 13:04:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.073 |  |
| 2026-06-30 13:03:41 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.080 |  |
| 2026-06-30 13:06:31 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.136 |  |
| 2026-06-30 13:04:37 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)