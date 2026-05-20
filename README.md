# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_18:35:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 18:35:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-20 18:12:51 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.036 |  |
| 2026-05-20 18:11:52 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 18:11:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 18:07:59 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-05-20 18:07:20 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:07:08 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:07:07 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:06:16 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:05:06 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:50 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:49 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.023 |  |
| 2026-05-20 18:04:28 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.096 |  |
| 2026-05-20 18:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:05 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:49 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 18:03:49 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:39 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-05-20 18:03:35 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:28 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:26 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-05-20 18:03:09 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:04 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-20 18:02:56 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 18:01:53 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 18:01:36 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-20 18:01:29 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 18:03:39 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-05-20 18:03:04 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-20 18:00:28 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-20 18:01:36 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-20 18:01:53 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 18:03:49 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 18:11:52 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-20 18:35:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-20 18:11:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:00:15 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:05 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:05:06 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:00:50 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:09 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:06:16 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:07:20 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:07 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:04 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:01:29 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:07:08 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:49 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:04:50 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:35 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:03:28 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-20 18:07:59 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-05-20 18:07:07 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:02:56 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-20 18:03:26 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-05-20 18:01:18 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-05-20 18:04:49 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.023 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-20 18:12:51 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.036 |  |
| 2026-05-20 18:00:39 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.062 |  |
| 2026-05-20 18:04:28 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)