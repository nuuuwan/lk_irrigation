# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_11:22:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 11:22:23 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.002 |  |
| 2026-02-04 11:08:38 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-02-04 11:07:19 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-02-04 11:07:05 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-04 11:05:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:05:40 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:05:26 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.022 |  |
| 2026-02-04 11:05:21 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.049 |  |
| 2026-02-04 11:05:05 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:04:46 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-04 11:04:44 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:04:26 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.038 |  |
| 2026-02-04 11:04:16 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:03:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:03:42 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:03:16 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 11:03:06 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:36 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:30 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 11:02:12 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-02-04 11:01:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:01:40 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-04 11:01:32 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:01:09 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-02-04 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:00:55 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:00:51 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 11:04:46 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 11:01:40 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-04 11:07:05 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-04 11:02:30 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 11:03:16 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 11:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:36 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:03:42 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:09:30 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:03:06 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:05:40 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:01:25 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:04:44 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:05:05 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:02:12 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 10:13:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:00:55 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 11:22:23 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.002 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 11:05:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:04:16 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:03:52 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:01:32 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-04 11:01:09 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-02-04 11:08:38 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.014 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-04 11:05:26 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.022 |  |
| 2026-02-04 11:07:19 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-02-04 11:04:26 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.038 |  |
| 2026-02-04 11:02:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-02-04 11:00:51 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.044 |  |
| 2026-02-04 11:05:21 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.049 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)