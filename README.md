# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_16:14:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,842 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 16:14:42 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 16:13:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:12:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:12:13 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:12:12 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:11:47 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-18 16:09:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-18 16:09:30 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-18 16:09:07 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-18 16:07:56 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:07:08 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:06:28 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:06:10 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:05:43 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:59 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.042 |  |
| 2026-06-18 16:04:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:04:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:31 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:19 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-18 16:04:15 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:03:54 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-06-18 16:03:28 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:03:24 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-18 16:03:19 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-06-18 16:03:14 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:03:11 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:51 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:44 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-06-18 16:02:35 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:32 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:19 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-18 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-18 16:02:13 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:12 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:03 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:35 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:13 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 16:03:19 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-06-18 15:02:50 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-18 16:03:24 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-18 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.75 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-18 16:09:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-18 16:02:19 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-18 16:04:19 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-18 16:11:47 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-18 16:09:30 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-18 16:14:42 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 16:07:08 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:03:28 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 16:01:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:12:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 15:02:41 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:35 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:15 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:55 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:51 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:03:14 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:03 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:01:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:13:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:07:56 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:04:31 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:05:43 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:02:32 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 16:09:07 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-18 16:04:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:03:11 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:35 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:12 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:13 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-18 16:02:44 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-06-18 16:03:54 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-06-18 16:01:13 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.021 |  |
| 2026-06-18 16:04:59 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)