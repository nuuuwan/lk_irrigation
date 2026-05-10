# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_21:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 21:03:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:03:24 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-05-10 21:03:16 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:03:12 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-10 21:02:52 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 21:02:28 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 21:02:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-10 21:02:24 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 21:02:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-10 21:01:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:01:43 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:06 | Wellawaya (Kirindi Oya) | 3.35 | 🟢 Normal | 1.517 | 🔺 Rising |
| 2026-05-10 21:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-05-10 21:00:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:00:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 20:26:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 20:14:40 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-10 20:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.067 |  |
| 2026-05-10 20:11:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 21:01:06 | Wellawaya (Kirindi Oya) | 3.35 | 🟢 Normal | 1.517 | 🔺 Rising |
| 2026-05-10 20:03:06 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-05-10 21:03:24 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-05-10 20:14:40 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-10 21:03:12 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-10 21:02:28 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 20:10:10 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-10 20:02:41 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 21:00:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 21:02:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-10 20:00:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-10 21:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 20:05:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-10 20:26:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 21:02:24 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 20:02:55 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 20:05:46 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-10 20:05:11 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 20:02:11 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:03:30 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 20:03:23 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:01:43 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:02:52 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 20:07:07 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-05-10 20:02:17 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:03:16 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:00:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 20:07:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-05-10 21:02:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-10 20:06:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-05-10 21:01:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-05-10 20:06:48 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-05-10 20:03:35 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.049 |  |
| 2026-05-10 20:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)