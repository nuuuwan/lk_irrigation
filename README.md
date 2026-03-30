# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_09:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,313 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 09:12:10 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:11:51 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-03-30 09:11:31 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:07:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-03-30 09:07:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-30 09:06:11 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:06:06 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:06:01 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:05:42 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:05:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:05:25 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.230 |  |
| 2026-03-30 09:04:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:04:11 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:49 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:03:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.051 |  |
| 2026-03-30 09:03:40 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 09:03:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:20 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:03:15 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:03:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:09 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:03 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:55 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:02:52 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-30 09:02:33 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:25 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:02:23 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:13 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-30 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-30 09:02:07 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-30 09:02:06 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:02 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.049 |  |
| 2026-03-30 09:01:03 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:00:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 08:59:02 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 09:07:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-30 09:02:52 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-30 09:02:07 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-30 09:02:13 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-30 09:03:40 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-30 09:02:55 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:03:15 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:02:25 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:05:42 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 09:02:06 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:12:10 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 08:59:02 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:06:11 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:11:31 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:04:11 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:03 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:33 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:02:23 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:04:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:06:06 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:00:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:09 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:05:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 09:03:49 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:06:01 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:03:20 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-30 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-30 08:12:06 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.025 |  |
| 2026-03-30 09:11:51 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-03-30 08:12:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.044 |  |
| 2026-03-30 09:02:02 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.049 |  |
| 2026-03-30 09:07:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-03-30 09:03:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.051 |  |
| 2026-03-30 09:05:25 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)