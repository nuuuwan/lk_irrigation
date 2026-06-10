# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_05:14:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 05:14:26 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-11 05:14:24 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-11 05:12:22 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:10:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:09:24 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 05:08:58 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:08:48 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-06-11 05:07:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:07:44 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.005 |  |
| 2026-06-11 05:06:20 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:05:35 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:05:14 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:05:04 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:05:04 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:04:58 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:04:18 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:04:07 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:03:55 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:03:52 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 05:03:47 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:03:35 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.049 |  |
| 2026-06-11 05:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 05:03:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:59 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-11 05:02:33 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.039 |  |
| 2026-06-11 05:02:24 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-11 05:02:23 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-11 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:02:12 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 05:02:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:01:47 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-11 05:01:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:00:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 04:31:14 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 05:02:24 | Dunamale (Aththanagalu Oya) | 1.49 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-11 05:14:26 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-11 05:02:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-11 05:03:52 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 05:09:24 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 05:02:12 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 05:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 05:03:55 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:02:20 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:05:04 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 05:07:44 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.005 |  |
| 2026-06-11 04:08:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.004 |  |
| 2026-06-11 05:08:58 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:00:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:05:04 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:59 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:12:22 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:05:35 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:03:47 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:06:20 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:04:18 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:01:00 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:03:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:04:58 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:07:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:10:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 05:01:47 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-11 03:23:30 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.016 |  |
| 2026-06-11 04:13:37 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-06-11 05:08:48 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-11 05:02:33 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.039 |  |
| 2026-06-11 05:03:35 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.049 |  |
| 2026-06-11 04:11:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -3.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)