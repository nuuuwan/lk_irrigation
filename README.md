# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_06:26:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 06:26:09 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.002 |  |
| 2026-05-04 06:10:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 06:08:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-04 06:07:59 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.037 |  |
| 2026-05-04 06:07:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-05-04 06:07:24 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2026-05-04 06:07:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.123 |  |
| 2026-05-04 06:07:00 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:06:38 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:06:37 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-04 06:05:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:05:14 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-04 06:04:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-05-04 06:04:28 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:04:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-05-04 06:04:08 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-05-04 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-05-04 06:04:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-04 06:03:46 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:03:38 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:03:01 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:02:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.107 |  |
| 2026-05-04 06:02:26 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:02:25 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-04 06:02:20 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-05-04 06:02:09 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:35 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.071 |  |
| 2026-05-04 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-04 06:01:33 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-04 06:01:28 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:51 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:51 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-05-04 06:00:49 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:49 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.112 |  |
| 2026-05-04 06:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:10 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 06:04:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 2.118 | 🔺 Rising |
| 2026-05-04 06:06:37 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-04 06:04:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-04 06:01:33 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-04 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-04 06:10:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 06:08:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-04 06:05:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:03:01 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:02:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:02:09 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:06:38 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:51 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:10 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:04:28 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:42 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:03:46 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:01:28 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:07:00 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 06:26:09 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.002 |  |
| 2026-05-04 06:07:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-05-04 06:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:02:26 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:03:38 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-04 06:04:08 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-05-04 06:02:25 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-05-04 06:05:14 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-04 06:00:51 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-05-04 06:02:20 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-05-04 06:07:59 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.037 |  |
| 2026-05-04 06:01:35 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.071 |  |
| 2026-05-04 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-05-04 06:07:24 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.085 |  |
| 2026-05-04 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.107 |  |
| 2026-05-04 06:00:49 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.112 |  |
| 2026-05-04 06:07:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)