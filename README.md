# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_17:12:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,208 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 17:12:39 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:11:38 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 17:07:42 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 17:07:33 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:07:23 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:07:10 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-04 17:06:47 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-07-04 17:06:42 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 17:06:39 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:06:10 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:05:26 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 17:05:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.075 |  |
| 2026-07-04 17:05:04 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 17:04:22 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:04:11 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:04:08 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-07-04 17:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 17:04:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-04 17:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 17:03:19 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:03:17 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-07-04 17:03:02 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.305 | 🔺 Rising |
| 2026-07-04 17:02:45 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 17:02:44 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 17:02:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:02:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:02:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:52 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-04 17:01:39 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:19 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:07 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:01 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-04 17:00:35 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:34 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:17 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:16 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 17:03:02 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.305 | 🔺 Rising |
| 2026-07-04 17:03:17 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-07-04 17:01:52 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-04 17:06:42 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 17:00:16 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-04 17:05:04 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 17:02:45 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-04 17:02:44 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 17:04:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-04 17:01:01 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-04 16:09:22 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 17:05:26 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 17:11:38 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 17:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 17:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 17:07:42 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 17:00:17 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:02:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:12:39 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:04:22 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 16:00:30 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:39 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:35 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:07 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:06:10 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:02:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:02:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:06:39 | Holombuwa (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:01:19 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:00:34 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:07:23 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:03:19 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:04:11 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 17:06:47 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-07-04 17:07:10 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-04 17:04:08 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-07-04 17:05:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)