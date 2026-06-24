# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_04:01:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 04:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 04:01:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 03:33:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 03:33:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 03:33:04 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 03:19:15 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:11:09 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.018 |  |
| 2026-06-25 03:11:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 04:01:23 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-25 03:04:56 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 04:01:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 03:01:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 03:01:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-25 03:00:40 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:43 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:04:07 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:03:12 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:03:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:11:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:20 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:27 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:08:06 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:19:15 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:07:24 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:06:00 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 03:02:46 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:13:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-06-25 03:04:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 03:05:46 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-25 03:11:09 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.018 |  |
| 2026-06-25 03:02:16 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-06-25 03:06:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-06-25 03:05:21 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-06-25 03:00:40 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.031 |  |
| 2026-06-25 03:02:12 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.053 |  |
| 2026-06-25 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.056 |  |
| 2026-06-25 03:05:15 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.070 |  |
| 2026-06-25 03:05:52 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.082 |  |
| 2026-06-25 03:06:41 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.117 |  |
| 2026-06-25 02:02:50 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.255 |  |
| 2026-06-25 03:02:10 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -3.130 |  |
| 2026-06-25 03:08:31 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -5.684 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)