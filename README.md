# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_02:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 02:10:50 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 02:07:51 | Rathnapura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.060 |  |
| 2026-05-13 02:06:59 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 02:06:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.102 |  |
| 2026-05-13 02:06:35 | Siyambalanduwa (Heda Oya) | 1.57 | 🟢 Normal | -0.862 |  |
| 2026-05-13 02:06:18 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.015 |  |
| 2026-05-13 02:05:49 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 02:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-13 02:04:38 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 02:04:32 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.039 |  |
| 2026-05-13 02:04:26 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2026-05-13 02:04:16 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-05-13 02:03:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-05-13 02:03:19 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-05-13 02:03:16 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-13 02:03:09 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-05-13 02:03:08 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.005 |  |
| 2026-05-13 02:02:38 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-05-13 02:02:28 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 02:02:11 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-13 02:02:09 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-13 02:01:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-13 02:00:52 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 02:04:16 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-05-13 02:04:38 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-13 02:05:49 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 02:06:59 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-13 00:11:51 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-13 01:26:44 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 01:05:32 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 02:00:52 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:05:49 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 02:10:50 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 02:03:16 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:32:49 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 02:03:08 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.005 |  |
| 2026-05-13 02:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.009 |  |
| 2026-05-13 02:03:19 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-05-13 02:02:11 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-13 02:02:28 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:04:49 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-13 02:02:38 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-05-13 02:06:18 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.015 |  |
| 2026-05-13 01:06:53 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-13 02:02:09 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-05-13 01:03:55 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-13 01:00:27 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-13 02:03:09 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 02:04:32 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | -0.039 |  |
| 2026-05-13 02:04:26 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.040 |  |
| 2026-05-13 02:01:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-13 02:03:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-05-13 02:07:51 | Rathnapura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.060 |  |
| 2026-05-13 01:06:47 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.065 |  |
| 2026-05-13 02:06:41 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.102 |  |
| 2026-05-13 01:02:13 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.119 |  |
| 2026-05-13 01:09:40 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.126 |  |
| 2026-05-13 02:06:35 | Siyambalanduwa (Heda Oya) | 1.57 | 🟢 Normal | -0.862 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)