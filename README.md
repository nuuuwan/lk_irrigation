# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_18:28:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 18:28:43 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.057 |  |
| 2026-01-04 18:27:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-04 18:23:00 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-04 18:07:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:06:17 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:05:53 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-01-04 18:05:16 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:05:08 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-04 18:04:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:51 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.028 |  |
| 2026-01-04 18:03:51 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-01-04 18:03:50 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:03:49 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:42 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:36 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:33 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:25 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:13 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 18:03:10 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:59 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:02:52 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:52 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.077 |  |
| 2026-01-04 18:02:37 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:18 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-04 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.044 |  |
| 2026-01-04 18:02:08 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:57 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:37 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:09 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:00:41 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.082 |  |
| 2026-01-04 18:00:30 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 18:02:18 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-04 18:27:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-04 18:03:13 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 18:02:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:00:30 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:09 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:36 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:33 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:05:16 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:56 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:04:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:10 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:04 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:42 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:08 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:03:49 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:06:17 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:52 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:07:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:01:37 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:05:08 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-04 17:02:33 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:03:50 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:01:07 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:02:59 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-04 18:23:00 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-01-04 18:03:51 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-01-04 18:03:51 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.028 |  |
| 2026-01-04 18:02:37 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-01-04 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.044 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-04 18:28:43 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.057 |  |
| 2026-01-04 18:05:53 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-01-04 18:02:52 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.077 |  |
| 2026-01-04 18:00:41 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)