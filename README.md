# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_13:23:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,936 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 13:23:36 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:23:10 | Baddegama (Gin Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:22:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:10:29 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:09:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:07:55 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:06:03 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.060 |  |
| 2026-03-16 13:05:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:05:13 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-16 13:03:16 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:03:11 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:03:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:02:57 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-16 13:02:57 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-16 13:02:37 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:02:18 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:02:15 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:02:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-16 13:01:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:01:35 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:33 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-16 13:01:31 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.039 |  |
| 2026-03-16 13:01:19 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:19 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:08 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:05 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:00:43 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:00:26 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-16 13:00:14 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.060 |  |
| 2026-03-16 13:00:14 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 13:02:57 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-16 13:02:57 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-16 13:02:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-16 13:00:26 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-16 13:00:14 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-16 13:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-16 13:01:05 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:05:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 13:01:19 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:31 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:35 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:22:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:23:36 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:57 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:10:29 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:23:10 | Baddegama (Gin Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:08:49 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:28 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:00:43 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:08 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:03:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:01:19 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:07:55 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:02:18 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:05:13 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:02:15 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-16 13:09:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:03:16 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:03:11 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:02:37 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-03-16 13:01:33 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-16 12:11:34 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-16 13:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.039 |  |
| 2026-03-16 13:06:03 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.060 |  |
| 2026-03-16 13:00:14 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)