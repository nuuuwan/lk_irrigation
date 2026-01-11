# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_18:13:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 18:13:23 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:12:03 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-01-11 18:05:33 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:05:23 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 18:05:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 18:05:10 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:05:02 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:04:26 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 18:04:25 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:04:19 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:04:09 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-11 18:03:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.020 |  |
| 2026-01-11 18:03:24 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:03 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:02 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-11 18:02:42 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:26 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:04 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 18:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-11 18:01:55 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 18:01:48 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:29 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 18:01:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.081 |  |
| 2026-01-11 18:01:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:51 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-01-11 18:00:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 18:00:13 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-11 17:59:52 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 18:12:03 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.887 | 🔺 Rising |
| 2026-01-11 18:00:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-11 18:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-11 18:04:09 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-11 18:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 18:02:04 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 18:05:23 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 18:01:29 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 18:04:26 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 18:05:15 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:13 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:17:56 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:55 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:05:10 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:42 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:26 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:02 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:48 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:05:33 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:13:23 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:05:02 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:03 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:24 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:03:10 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:04:25 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:00:50 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-01-11 18:03:54 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.020 |  |
| 2026-01-11 17:59:52 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-01-11 18:00:51 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-01-11 18:01:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)