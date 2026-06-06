# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_21:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 21:11:28 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-06-06 21:08:41 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.094 |  |
| 2026-06-06 21:07:45 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 21:07:10 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:07:09 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2026-06-06 21:06:58 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:42 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.029 |  |
| 2026-06-06 21:06:23 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:05:48 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-06-06 21:05:40 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.051 |  |
| 2026-06-06 21:05:31 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:05:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-06-06 21:04:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:48 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:39 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-06-06 21:04:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:04:04 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:35 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:03:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2026-06-06 21:02:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:16 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:32 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 21:07:45 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:06:23 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:02:16 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:42 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:04 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:58 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:35 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:05:31 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:11:28 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.009 |  |
| 2026-06-06 21:04:48 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:03:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:07:10 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:04:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:05:48 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-06-06 21:04:39 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-06-06 21:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.029 |  |
| 2026-06-06 21:07:09 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.039 |  |
| 2026-06-06 21:01:32 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:05:40 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.051 |  |
| 2026-06-06 21:05:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-06-06 21:02:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2026-06-06 21:08:41 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)