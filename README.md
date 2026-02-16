# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_11:17:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 11:17:05 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:13:38 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:10:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.119 |  |
| 2026-02-16 11:09:10 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-02-16 11:08:07 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-16 11:07:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-16 11:06:45 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:34 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:17 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:16 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:04:32 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-16 11:04:16 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-02-16 11:04:02 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 11:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-02-16 11:03:48 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:03:35 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:03:29 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-02-16 11:03:25 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:03:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:47 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-02-16 11:02:44 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:34 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-16 11:02:26 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:25 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | 0.637 | 🔺 Rising |
| 2026-02-16 11:02:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:54 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:54 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:35 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:21 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-16 11:01:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 11:01:14 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:14 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 11:02:25 | Weraganthota (Mahaweli Ganga) | -2.09 | 🟢 Normal | 0.637 | 🔺 Rising |
| 2026-02-16 11:04:16 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-02-16 11:07:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-16 11:07:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-16 11:01:21 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-16 11:02:34 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-16 11:04:02 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-16 11:04:32 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-16 11:01:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 11:01:35 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:11:08 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:34 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:06:45 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:16 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:03:25 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:03:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:17:05 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:54 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:54 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:17 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:08:07 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:02:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:05:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:14 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:53 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:03:35 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:01:14 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 11:13:38 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:57 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:03:48 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:44 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:02:26 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-02-16 11:09:10 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-02-16 11:02:47 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-02-16 11:03:29 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.029 |  |
| 2026-02-16 11:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.029 |  |
| 2026-02-16 11:10:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)