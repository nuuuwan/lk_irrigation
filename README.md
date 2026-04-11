# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_11:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 11:12:16 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-11 11:11:35 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-11 11:11:25 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-11 11:10:40 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.017 |  |
| 2026-04-11 11:09:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-11 11:09:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 11:09:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:09:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:08:04 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-04-11 11:05:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-11 11:05:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-11 11:03:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:03:46 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.034 |  |
| 2026-04-11 11:03:24 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:21 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-04-11 11:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:03:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-04-11 11:03:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:04 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:58 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:43 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-11 11:02:41 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:37 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:02:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.037 |  |
| 2026-04-11 11:01:37 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-04-11 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 11:01:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:00:53 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:00:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:00:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 11:00:16 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 11:01:37 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-04-11 11:05:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-11 11:09:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-11 10:16:02 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-11 11:09:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-11 11:05:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-11 11:11:35 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-11 11:02:43 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-11 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-11 11:11:25 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-11 11:00:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 11:12:16 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-11 11:00:16 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:00:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:24 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:10 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:41 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-04-11 10:07:05 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:01:22 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:09:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:04 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:37 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:00:53 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:58 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-11 11:03:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-04-11 11:08:04 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-04-11 11:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:02:17 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:03:48 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:09:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-11 11:10:40 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.017 |  |
| 2026-04-11 11:03:46 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.034 |  |
| 2026-04-11 11:01:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.037 |  |
| 2026-04-11 11:03:21 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)