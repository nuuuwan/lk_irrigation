# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_02:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,057 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 02:20:37 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.131 |  |
| 2026-06-30 02:18:48 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:12:09 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:11:12 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-30 02:09:56 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | -0.022 |  |
| 2026-06-30 02:09:51 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-30 02:07:37 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.067 |  |
| 2026-06-30 02:07:32 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:07:32 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-06-30 02:06:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-06-30 02:05:57 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-06-30 02:05:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.176 |  |
| 2026-06-30 02:05:45 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:05:39 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-06-30 02:05:07 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.122 |  |
| 2026-06-30 02:04:30 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 02:04:23 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.071 |  |
| 2026-06-30 02:03:47 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:03:05 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-06-30 02:03:05 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:37 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 02:02:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:36 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-30 02:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 02:02:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-06-30 02:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.005 |  |
| 2026-06-30 02:01:46 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-30 02:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-06-30 02:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:01:15 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-30 02:01:03 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.055 |  |
| 2026-06-30 02:00:58 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:00:57 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-06-30 01:53:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:41:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.269 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 02:02:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-06-30 02:09:51 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-30 02:02:36 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-30 02:01:15 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-30 02:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 02:04:30 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 02:11:12 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-30 02:02:37 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:05:45 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:03:05 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:03:47 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:53:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:51 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:00:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:18:48 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:00:58 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:12:09 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:07:32 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 02:02:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.005 |  |
| 2026-06-30 02:07:32 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-06-30 02:01:46 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-30 02:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-06-30 02:06:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-06-30 02:05:57 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-06-30 02:00:57 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-06-30 02:09:56 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | -0.022 |  |
| 2026-06-30 02:03:05 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-06-30 02:05:39 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-06-30 02:01:03 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.055 |  |
| 2026-06-30 02:07:37 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.067 |  |
| 2026-06-30 02:04:23 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.071 |  |
| 2026-06-30 02:05:07 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.122 |  |
| 2026-06-30 02:20:37 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.131 |  |
| 2026-06-30 02:05:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)