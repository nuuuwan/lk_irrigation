# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_04:17:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 04:17:00 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.065 |  |
| 2026-05-10 04:16:10 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.136 |  |
| 2026-05-10 04:12:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.062 |  |
| 2026-05-10 04:09:01 | Thanamalwila (Kirindi Oya) | 3.65 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-10 04:07:08 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-05-10 04:06:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-10 04:06:08 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:06:04 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.038 |  |
| 2026-05-10 04:05:53 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-05-10 04:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-10 04:05:42 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.048 |  |
| 2026-05-10 04:04:38 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-10 04:03:49 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 04:03:34 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:03:32 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-05-10 04:03:20 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.024 |  |
| 2026-05-10 04:03:14 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:03:08 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 04:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 04:02:31 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-10 04:02:26 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | -0.222 |  |
| 2026-05-10 04:02:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -1.037 |  |
| 2026-05-10 04:02:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2026-05-10 04:02:12 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 04:02:08 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.042 |  |
| 2026-05-10 04:02:01 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.011 |  |
| 2026-05-10 04:01:50 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-05-10 04:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-10 04:01:12 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.044 |  |
| 2026-05-10 04:01:12 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:01:04 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 04:01:50 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-05-10 04:06:10 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 04:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-10 04:01:04 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 04:09:01 | Thanamalwila (Kirindi Oya) | 3.65 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-10 04:02:12 | Katharagama (Menik Ganga) | 1.61 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 04:03:08 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 04:03:49 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:01:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-10 04:02:31 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-10 04:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 03:04:51 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 02:02:31 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:03:34 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:06:08 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:03:14 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:01:12 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-05-10 04:02:01 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.011 |  |
| 2026-05-10 04:04:38 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-10 04:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-10 04:03:20 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.024 |  |
| 2026-05-10 04:06:04 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.038 |  |
| 2026-05-10 04:05:53 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-05-10 04:02:08 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.042 |  |
| 2026-05-10 04:01:12 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.044 |  |
| 2026-05-10 04:05:42 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.048 |  |
| 2026-05-10 04:03:32 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 04:02:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2026-05-10 04:12:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.062 |  |
| 2026-05-10 04:17:00 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.065 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 04:07:08 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-05-10 04:16:10 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.136 |  |
| 2026-05-10 03:03:45 | Moragaswewa (Deduru Oya) | 3.48 | 🟢 Normal | -0.141 |  |
| 2026-05-10 04:02:26 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | -0.222 |  |
| 2026-05-10 04:02:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -1.037 |  |
| 2026-05-10 03:16:57 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -3.273 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)