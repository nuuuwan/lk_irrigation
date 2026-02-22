# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_21:07:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 21:07:09 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 21:06:32 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:06:21 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.123 |  |
| 2026-02-22 21:05:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-02-22 21:05:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.057 |  |
| 2026-02-22 21:05:47 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-02-22 21:05:19 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-02-22 21:05:09 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.105 |  |
| 2026-02-22 21:05:07 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.095 |  |
| 2026-02-22 21:04:53 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:04:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:04:27 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-02-22 21:03:56 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:03:49 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:03:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:03:27 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-02-22 21:03:19 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:59 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.042 |  |
| 2026-02-22 21:02:56 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.117 |  |
| 2026-02-22 21:02:52 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | -0.061 |  |
| 2026-02-22 21:02:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-22 21:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 21:02:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:05 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-02-22 21:01:28 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-02-22 21:01:15 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 21:01:08 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.034 |  |
| 2026-02-22 21:00:46 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 21:00:32 | Manampitiya (Mahaweli Ganga) | 3.23 | 🟡 Alert | -0.146 |  |
| 2026-02-22 20:17:48 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.025 |  |
| 2026-02-22 20:15:57 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 21:00:32 | Manampitiya (Mahaweli Ganga) | 3.23 | 🟡 Alert | -0.146 |  |
| 2026-02-22 21:00:46 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 21:07:09 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 21:01:15 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 21:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 21:03:49 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:04:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 20:05:01 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:02:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:06:32 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:04:53 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-22 21:03:56 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:03:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2026-02-22 21:01:28 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-02-22 21:02:32 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-02-22 20:15:57 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-02-22 21:05:19 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-02-22 21:03:27 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-02-22 21:01:08 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.034 |  |
| 2026-02-22 20:09:24 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.038 |  |
| 2026-02-22 21:04:27 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-02-22 21:02:59 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.042 |  |
| 2026-02-22 20:06:11 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.044 |  |
| 2026-02-22 21:05:47 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-02-22 20:07:00 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.051 |  |
| 2026-02-22 21:05:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.057 |  |
| 2026-02-22 21:02:52 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | -0.061 |  |
| 2026-02-22 21:02:05 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.081 |  |
| 2026-02-22 21:05:07 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.095 |  |
| 2026-02-22 21:05:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-02-22 21:05:09 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.105 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 21:02:56 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.117 |  |
| 2026-02-22 21:06:21 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)