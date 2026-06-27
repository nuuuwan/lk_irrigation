# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_06:24:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 06:24:58 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:19:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-06-27 06:13:43 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-06-27 06:10:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:09:13 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.047 |  |
| 2026-06-27 06:09:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 06:08:59 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:08:23 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:08:06 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -5.775 |  |
| 2026-06-27 06:07:00 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:06:31 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:06:27 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.049 |  |
| 2026-06-27 06:06:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:05:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.037 |  |
| 2026-06-27 06:05:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:04:59 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -5.775 |  |
| 2026-06-27 06:04:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 06:04:52 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:04:24 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 06:04:19 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-27 06:04:18 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:04:08 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-27 06:03:47 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -72.000 |  |
| 2026-06-27 06:03:46 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -72.000 |  |
| 2026-06-27 06:03:33 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-27 06:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:03:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-27 06:02:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-27 06:02:15 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.060 |  |
| 2026-06-27 06:01:59 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 06:01:46 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.002 |  |
| 2026-06-27 06:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:44 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-06-27 06:01:36 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:00:52 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:00:27 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 05:59:59 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 06:03:33 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-27 06:01:36 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:07:00 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:06:31 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-27 06:09:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 06:04:57 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 06:01:59 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 06:04:24 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 05:59:59 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:00:27 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:10:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:36 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:06:06 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:08:23 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:24:58 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:00:52 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:04:18 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:05:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:08:59 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:04:52 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:46 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.002 |  |
| 2026-06-27 06:03:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-27 06:04:19 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-27 05:02:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-27 06:02:33 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-06-27 06:19:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-06-27 06:04:08 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-27 06:05:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.037 |  |
| 2026-06-27 06:13:43 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-06-27 06:09:13 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.047 |  |
| 2026-06-27 06:06:27 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.049 |  |
| 2026-06-27 06:01:44 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-06-27 06:02:15 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | -0.060 |  |
| 2026-06-27 06:08:06 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -5.775 |  |
| 2026-06-27 06:03:47 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)