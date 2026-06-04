# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_05:26:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 05:26:40 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:26:39 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:26:21 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:26:06 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-06-04 05:24:31 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 05:21:52 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 05:16:15 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:14:39 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-06-04 05:12:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.082 |  |
| 2026-06-04 05:07:58 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-04 05:07:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-04 05:07:16 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-04 05:06:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-04 05:05:45 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:05:37 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 05:05:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:05:24 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -1.575 |  |
| 2026-06-04 05:05:05 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:56 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-04 05:04:39 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:38 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:21 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 05:04:06 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-04 05:04:04 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -1.575 |  |
| 2026-06-04 05:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 05:03:55 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.973 |  |
| 2026-06-04 05:03:30 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:03:18 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.973 |  |
| 2026-06-04 05:03:04 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:02:44 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:02:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-04 05:02:13 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:02:09 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-04 05:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:01:31 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:01:28 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.080 |  |
| 2026-06-04 05:00:39 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 03:47:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 2.323 | 🔺 Rising |
| 2026-06-04 05:07:58 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-04 05:04:06 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-04 05:02:09 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-04 05:07:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-04 04:04:19 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 05:07:16 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-04 05:06:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-04 05:21:52 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-04 05:24:31 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 05:05:37 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 05:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 05:04:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:05:28 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:00:39 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:16:15 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:03:04 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:26:40 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:39 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:05:45 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:01:31 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:05:05 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:02:13 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:03:30 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:38 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:21 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 03:02:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-04 05:04:56 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-04 05:02:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-04 05:26:06 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-06-04 05:14:39 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-06-04 05:01:28 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.080 |  |
| 2026-06-04 05:12:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.082 |  |
| 2026-06-04 05:03:55 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.973 |  |
| 2026-06-04 05:05:24 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -1.575 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)