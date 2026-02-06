# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_14:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 14:13:37 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:11:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:11:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.117 |  |
| 2026-02-06 14:10:35 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-06 14:08:54 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:08:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-06 14:08:09 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.094 |  |
| 2026-02-06 14:07:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:07:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.028 |  |
| 2026-02-06 14:06:51 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 14:05:55 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:05:45 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:05:36 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-02-06 14:05:26 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 14:05:16 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:04:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-02-06 14:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-02-06 14:02:54 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 14:02:41 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:41 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:25 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:14 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-06 14:02:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:05 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.131 |  |
| 2026-02-06 14:01:43 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:39 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:39 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 14:01:39 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-02-06 14:01:22 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:10 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:06 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-06 14:00:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:26:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.117 |  |
| 2026-02-06 13:23:45 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:20:14 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-06 13:19:29 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 14:04:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-02-06 14:01:06 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 14:08:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-06 14:01:39 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 14:05:26 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 14:02:14 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-06 14:02:54 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 14:06:51 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 12:10:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-06 14:01:43 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:22 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:13:37 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:05:45 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:11:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:00:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:05:55 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:41 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:41 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:07:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:08:54 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:10 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:01:39 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:02:25 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:05:16 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-06 14:10:35 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-06 14:01:39 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-02-06 14:07:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.028 |  |
| 2026-02-06 14:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-02-06 14:05:36 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 14:08:09 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.094 |  |
| 2026-02-06 14:11:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.117 |  |
| 2026-02-06 14:02:05 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)