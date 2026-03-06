# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_08:20:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 08:20:19 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:18:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:16:39 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:11:47 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:34 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:23 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:07:37 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-03-06 08:07:01 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.142 |  |
| 2026-03-06 08:06:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:06:33 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:05:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-06 08:05:56 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-06 08:04:33 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:04:20 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:04:08 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:31 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:31 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.153 |  |
| 2026-03-06 08:03:17 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:13 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.069 |  |
| 2026-03-06 08:02:59 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:02:40 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.032 |  |
| 2026-03-06 08:02:31 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-06 08:02:26 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:02:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:02:05 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 08:02:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-06 08:01:56 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 08:01:52 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 08:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.021 |  |
| 2026-03-06 08:01:26 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-06 08:01:24 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.112 |  |
| 2026-03-06 08:01:13 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:00:33 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 08:05:56 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-06 08:01:56 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-06 08:05:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-06 08:02:05 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 08:02:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-06 08:01:52 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 08:02:59 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:13 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:24 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:04:33 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:02:26 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 07:16:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:34 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:11:47 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:23 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:17 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:31 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:04:08 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:18:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:06:33 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:00:33 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:02:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:03:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:04:20 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:06:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:20:19 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:09:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:01:26 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-06 08:02:31 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-06 08:01:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.021 |  |
| 2026-03-06 08:07:37 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-03-06 08:02:40 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.032 |  |
| 2026-03-06 08:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.069 |  |
| 2026-03-06 08:01:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.112 |  |
| 2026-03-06 08:07:01 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.142 |  |
| 2026-03-06 08:03:31 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)