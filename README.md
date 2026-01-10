# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_09:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 09:10:51 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:09:40 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-10 09:08:49 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-01-10 09:08:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.005 |  |
| 2026-01-10 09:07:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:07:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:06:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-01-10 09:06:50 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:06:42 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:06:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-01-10 09:06:22 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:52 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:43 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:40 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:33 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:04:56 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:04:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:04:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:04:04 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-01-10 09:03:57 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:03:48 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 09:03:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.050 |  |
| 2026-01-10 09:03:41 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:03:35 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.014 |  |
| 2026-01-10 09:03:07 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-01-10 09:03:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-10 09:03:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:02:59 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:02:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:02:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:02:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-01-10 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.060 |  |
| 2026-01-10 09:01:58 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:01:56 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-01-10 09:01:23 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:01:15 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:01:12 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.120 |  |
| 2026-01-10 09:01:01 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 09:01:56 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-01-10 09:09:40 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-10 09:03:48 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-10 09:01:23 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:04:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:01:15 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 09:04:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:02:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:03:57 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:07:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:06:42 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:52 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:02:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:01:58 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:43 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:06:22 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:33 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:04:56 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:40 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:03:41 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:10:51 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:01:01 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:07:19 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:08:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.005 |  |
| 2026-01-10 09:02:59 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:03:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:06:50 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-10 09:08:49 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-01-10 09:03:35 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.014 |  |
| 2026-01-10 09:06:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-01-10 09:03:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-10 09:02:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-01-10 09:04:04 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-01-10 09:03:45 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.050 |  |
| 2026-01-10 09:03:07 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-01-10 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.060 |  |
| 2026-01-10 09:06:59 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-01-10 09:01:12 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)