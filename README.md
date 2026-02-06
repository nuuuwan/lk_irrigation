# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_12:16:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 12:16:13 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-06 12:14:12 | Panadugama (Nilwala Ganga) | 0.38 | 🟢 Normal | -318.857 |  |
| 2026-02-06 12:13:51 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -318.857 |  |
| 2026-02-06 12:10:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-06 12:09:11 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:08:27 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 12:08:20 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:07:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:05:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:04:46 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 12:04:37 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:04:18 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-02-06 12:03:41 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:03:34 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 12:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 12:03:31 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:30 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:03:03 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.030 |  |
| 2026-02-06 12:03:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:02:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:41 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:28 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:13 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 12:02:12 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:06 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:01:53 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:01:53 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:01:45 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.141 |  |
| 2026-02-06 12:01:39 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.084 |  |
| 2026-02-06 12:01:30 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 12:01:13 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:01:09 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:01:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.203 |  |
| 2026-02-06 12:00:48 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:00:45 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 12:16:13 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 12:04:46 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 12:08:27 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-06 12:02:13 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 12:03:34 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-06 12:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-06 12:01:30 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 12:10:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-06 12:01:09 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:05:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:04:18 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:57 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:07:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:04:37 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:31 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:06 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:02:28 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 11:23:15 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:08:20 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:09:11 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-06 12:03:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:01:13 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:03:30 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-06 12:00:48 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:03:41 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:01:53 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-06 12:03:03 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.030 |  |
| 2026-02-06 12:03:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 12:01:39 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.084 |  |
| 2026-02-06 12:01:45 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.141 |  |
| 2026-02-06 12:01:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.203 |  |
| 2026-02-06 12:14:12 | Panadugama (Nilwala Ganga) | 0.38 | 🟢 Normal | -318.857 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)