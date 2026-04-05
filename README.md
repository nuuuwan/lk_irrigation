# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_17:27:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 17:27:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:14:22 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 17:12:33 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:12:06 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:10:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:09:35 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:08:47 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:08:40 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:08:28 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:08:03 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | -0.072 |  |
| 2026-04-05 17:07:45 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.023 |  |
| 2026-04-05 17:07:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:07:36 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:06:45 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:06:18 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-05 17:06:15 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:05:51 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-04-05 17:04:37 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:04:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:03:35 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:03:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.043 |  |
| 2026-04-05 17:02:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:53 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:02:52 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.029 |  |
| 2026-04-05 17:02:39 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:30 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:17 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:03 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.069 |  |
| 2026-04-05 17:02:00 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:01:57 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.065 |  |
| 2026-04-05 17:01:35 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:01:31 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:01:15 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-05 17:01:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:01:05 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:00:51 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-05 17:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 17:00:40 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-05 17:00:33 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:00:14 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 17:06:18 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-05 17:01:15 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-05 17:00:14 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-05 17:00:51 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-05 17:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 17:14:22 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 17:01:31 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:01:05 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:02:53 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 17:07:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:39 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:00:33 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:01:35 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:27:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:03:35 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:12:06 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:01:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:08:28 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:05:51 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:09:35 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:10:35 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:12:33 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:07:36 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:08:47 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:02:30 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 17:04:06 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:06:45 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:04:37 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:08:40 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:02:00 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-05 17:00:40 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-05 17:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-04-05 17:07:45 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.023 |  |
| 2026-04-05 17:02:52 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.029 |  |
| 2026-04-05 17:03:21 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.043 |  |
| 2026-04-05 17:01:57 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.065 |  |
| 2026-04-05 17:02:03 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.069 |  |
| 2026-04-05 17:08:03 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)