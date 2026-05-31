# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_01:37:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 01:37:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:37:18 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:12:43 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.026 |  |
| 2026-06-01 01:12:42 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:11:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-06-01 01:07:33 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-06-01 01:06:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:06:35 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:06:20 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.013 |  |
| 2026-06-01 01:05:53 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:05:38 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:05:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:04:56 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:04:33 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-01 01:04:18 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:04:18 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-01 01:03:59 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 01:03:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-06-01 01:03:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 01:03:09 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.041 |  |
| 2026-06-01 01:03:04 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-06-01 01:02:57 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.159 |  |
| 2026-06-01 01:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | -0.046 |  |
| 2026-06-01 01:02:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:13 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:07 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:00:43 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:00:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 01:04:33 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-01 01:03:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 01:04:18 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-01 01:03:59 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:06:45 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:13 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:07 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:00:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:04:18 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:01:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:06:35 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:02:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:00:43 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:37:35 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:37:18 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:05:38 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:12:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:12:42 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:01:27 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-06-01 01:05:53 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:04:56 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:05:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:44 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-06-01 01:06:20 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.013 |  |
| 2026-06-01 01:07:33 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-06-01 01:11:49 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-06-01 01:03:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-06-01 01:12:43 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.026 |  |
| 2026-06-01 01:03:04 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-06-01 00:15:20 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-06-01 01:03:09 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.041 |  |
| 2026-06-01 01:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | -0.046 |  |
| 2026-06-01 01:02:57 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)