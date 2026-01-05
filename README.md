# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_11:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 11:11:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 11:10:54 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-01-05 11:10:27 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:08:24 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 11:08:07 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:07:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:06:58 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.009 |  |
| 2026-01-05 11:06:06 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:06:00 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-05 11:04:44 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-01-05 11:04:43 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:04:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.182 |  |
| 2026-01-05 11:04:14 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:03:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.049 |  |
| 2026-01-05 11:03:31 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 11:03:30 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-05 11:03:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-05 11:03:17 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:03:10 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:03:02 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:59 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:58 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:02:53 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 11:02:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-01-05 11:02:32 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:25 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 11:02:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-01-05 11:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:01:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:01:00 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-01-05 11:00:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 11:03:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-05 11:06:00 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-05 11:03:30 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-05 11:08:24 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 11:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 11:03:31 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 11:11:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 11:02:32 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:00:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:59 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:06:06 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-05 10:03:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:03:17 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:53 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:10:27 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:07:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:03:02 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:01:45 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:04:14 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:04:43 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:02:25 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 11:10:54 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-01-05 11:06:58 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.009 |  |
| 2026-01-05 11:03:10 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:08:07 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-01-05 11:02:58 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-05 10:07:25 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.014 |  |
| 2026-01-05 11:01:00 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-01-05 11:02:07 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-01-05 11:04:44 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-01-05 11:03:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.049 |  |
| 2026-01-05 11:02:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-01-05 10:03:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.072 |  |
| 2026-01-05 11:04:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)